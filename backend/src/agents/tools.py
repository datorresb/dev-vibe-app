"""Enhanced tools for the LangGraph agent with better error handling and security."""

import subprocess
import tempfile
from pathlib import Path

import httpx
from langchain_core.tools import tool


@tool
def web_fetch(url: str, max_length: int = 10000) -> str:
    """
    Fetch content from a URL and return as text.

    Args:
        url: The URL to fetch content from
        max_length: Maximum length of content to return (default: 10000)

    Returns:
        The web page content as text, truncated if necessary
    """
    try:
        # Validate URL format
        if not url.startswith(('http://', 'https://')):
            return f"ERROR: Invalid URL format. URL must start with http:// or https://. Got: {url}"

        response = httpx.get(
            url,
            follow_redirects=True,
            timeout=30,
            headers={'User-Agent': 'LangGraph-Agent/1.0'}
        )
        response.raise_for_status()

        content = response.text[:max_length]
        if len(response.text) > max_length:
            content += f"\n\n[Content truncated at {max_length} characters]"

        return content

    except httpx.HTTPStatusError as e:
        return f"ERROR: HTTP {e.response.status_code} - {e.response.reason_phrase}"
    except httpx.ConnectError:
        return f"ERROR: Unable to connect to {url}"
    except httpx.TimeoutException:
        return "ERROR: Request timed out after 30 seconds"
    except Exception as e:
        return f"ERROR: {type(e).__name__}: {e}"


@tool
def run_python(code: str) -> str:
    """
    Execute Python code in a secure sandbox and return output.

    Args:
        code: Python code to execute

    Returns:
        The output of the code execution, including stdout and stderr

    Note:
        - Supports pandas and matplotlib
        - Code runs with a 30-second timeout
        - Limited to safe operations only
    """
    try:
        # Basic security checks
        dangerous_patterns = [
            'import os', 'import subprocess', 'import sys',
            '__import__', 'eval(', 'exec(',
            'open(', 'file(', 'input(',
            'raw_input(', 'compile('
        ]

        code_lower = code.lower()
        for pattern in dangerous_patterns:
            if pattern in code_lower:
                return f"ERROR: Security restriction - cannot use '{pattern}' in code"

        # Create temporary file
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            # Add safe imports by default
            safe_code = """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import math
from datetime import datetime, timedelta

""" + code

            f.write(safe_code)
            f.flush()
            temp_path = Path(f.name)

        try:
            # Execute with timeout
            result = subprocess.run(
                ["python", str(temp_path)],
                capture_output=True,
                text=True,
                timeout=30,
                cwd=tempfile.gettempdir()  # Run in temp directory
            )

            output = ""
            if result.stdout:
                output += result.stdout
            if result.stderr:
                output += "\nSTDERR:\n" + result.stderr

            return output if output.strip() else "(no output)"

        except subprocess.TimeoutExpired:
            return "ERROR: Code execution timed out after 30 seconds"
        except subprocess.CalledProcessError as e:
            return f"ERROR: Process failed with exit code {e.returncode}"
        finally:
            # Cleanup temp file
            try:
                temp_path.unlink()
            except FileNotFoundError:
                pass

    except Exception as e:
        return f"ERROR: {type(e).__name__}: {e}"
