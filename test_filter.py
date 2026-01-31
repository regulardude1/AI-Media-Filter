"""Tests for the AI Media Filter."""
import pytest
from pathlib import Path
from filter import (
    AI_SIGNATURES,
    IMAGE_EXTENSIONS,
    AI_IMAGE_DIMENSIONS,
    identify_ai_tool,
    check_for_ai_signatures,
)


class TestAISignatures:
    """Test AI signature detection constants and logic."""
    
    def test_ai_signatures_not_empty(self):
        """Ensure we have AI signatures defined."""
        assert len(AI_SIGNATURES) > 0
    
    def test_common_signatures_present(self):
        """Check that common AI tool signatures are included."""
        signatures_lower = [s.lower() for s in AI_SIGNATURES]
        assert "stable diffusion" in signatures_lower
        assert "dall-e" in signatures_lower
        assert "midjourney" in signatures_lower
        assert "gemini" in signatures_lower


class TestImageExtensions:
    """Test image extension configuration."""
    
    def test_common_extensions_present(self):
        """Verify common image formats are supported."""
        assert ".png" in IMAGE_EXTENSIONS
        assert ".jpg" in IMAGE_EXTENSIONS
        assert ".jpeg" in IMAGE_EXTENSIONS
        assert ".webp" in IMAGE_EXTENSIONS


class TestAIDimensions:
    """Test AI image dimension detection."""
    
    def test_dalle3_dimensions_present(self):
        """DALL-E 3 standard sizes should be recognized."""
        assert (1024, 1024) in AI_IMAGE_DIMENSIONS
        assert (1024, 1792) in AI_IMAGE_DIMENSIONS
        assert (1792, 1024) in AI_IMAGE_DIMENSIONS
    
    def test_dalle2_dimensions_present(self):
        """DALL-E 2 sizes should be recognized."""
        assert (512, 512) in AI_IMAGE_DIMENSIONS
        assert (256, 256) in AI_IMAGE_DIMENSIONS


class TestIdentifyAITool:
    """Test AI tool identification logic."""
    
    def test_identifies_chatgpt(self):
        """Should identify ChatGPT/DALL-E 3 images."""
        result = identify_ai_tool(["c2pa"], "c2pa contentcredentials chatgpt")
        assert "ChatGPT" in result or "DALL-E" in result
    
    def test_identifies_gemini(self):
        """Should identify Google Gemini images."""
        result = identify_ai_tool(["gemini"], "made by google gemini imagen")
        assert "Gemini" in result
    
    def test_identifies_midjourney(self):
        """Should identify Midjourney images."""
        result = identify_ai_tool(["midjourney"], "midjourney --ar 16:9 --v 5")
        assert "Midjourney" in result
    
    def test_identifies_stable_diffusion(self):
        """Should identify Stable Diffusion images."""
        result = identify_ai_tool(["cfg scale"], "cfg scale: 7.5, steps: 20")
        assert "Stable Diffusion" in result


class TestCheckForSignatures:
    """Test the signature checking function."""
    
    def test_empty_metadata_returns_no_ai(self):
        """Empty metadata should not detect AI."""
        result = check_for_ai_signatures({}, Path("test.png"))
        assert result.is_ai is False
        assert result.confidence == "none"
    
    def test_detects_stable_diffusion_metadata(self):
        """Should detect Stable Diffusion parameters in metadata."""
        metadata = {
            "parameters": "steps: 20, cfg scale: 7.5, sampler: Euler"
        }
        result = check_for_ai_signatures(metadata, Path("test.png"))
        assert result.is_ai is True
        assert result.confidence in ["low", "medium", "high"]
