import pytest
from typing import Dict, Any, List

from app.utils.language_stats import get_language_resume

def test_get_language_resume_single_language():
    payload = {
        "repositories": {
            "nodes": [
                {
                    "languages": {
                        "edges": [
                            {
                                "size": 1000,
                                "node": {
                                    "name": "Python"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
    expected_result = [
        {
            "language": "Python",
            "size": 1000
        }
    ]

    result = get_language_resume(payload)

    assert result == expected_result

def test_get_language_resume_multi_language():
    payload = {
        "repositories": {
            "nodes": [
                {
                    "languages": {
                        "edges": [
                            {
                                "size": 1000,
                                "node": {
                                    "name": "Python"
                                }
                            },
                            {
                                "size": 1000,
                                "node": {
                                    "name": "JavaScript"
                                }
                            },
                            {
                                "size": 1000,
                                "node": {
                                    "name": "Cpp"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
    expected_result = [
        {
            "language": "Python",
            "size": 1000
        },
        {
            "language": "JavaScript",
            "size": 1000
        },
        {
            "language": "Cpp",
            "size": 1000
        }
    ]

    result = get_language_resume(payload)

    assert result == expected_result