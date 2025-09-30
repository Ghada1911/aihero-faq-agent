# Test Suite for FAQ Site Generator

This directory contains comprehensive tests for the `generate_website.py` script, organized into focused test files for maintainability and clarity.

## Test Structure

### Unit Tests (`tests/unit/`)
Tests for individual functions and components:

- **`test_frontmatter.py`** - YAML frontmatter parsing
  - Valid/invalid YAML handling
  - Edge cases (empty, malformed, special characters)
  - Multiline values and nested structures

- **`test_url_conversion.py`** - URL detection and conversion
  - HTTP/HTTPS URL detection
  - Code block and inline code preservation  
  - Trailing punctuation handling
  - Complex mixed scenarios

- **`test_markdown.py`** - Markdown processing
  - Basic markdown to HTML conversion
  - Image placeholder replacement
  - Table and task list processing
  - Syntax highlighting integration

- **`test_renderer.py`** - HighlightRenderer class
  - Language alias handling
  - Syntax highlighting functionality
  - Code span and link rendering
  - Error handling for invalid languages

- **`test_course_processing.py`** - Course and metadata processing
  - Course metadata loading
  - Section and question file processing
  - Error recovery and validation

- **`test_jinja_setup.py`** - Jinja2 template environment
  - Template loading and rendering
  - Custom filter functionality
  - Auto-escaping behavior

- **`test_sorting.py`** - Sorting and organization
  - Question sorting by sort_order
  - Section ordering by metadata
  - Handling missing sections

### Integration Tests (`tests/integration/`)
End-to-end workflow tests:

- **`test_site_generation.py`** - Complete site generation
  - Full pipeline from questions to HTML
  - Multiple course handling
  - Asset copying and file structure

- **`test_real_world.py`** - Real-world scenarios
  - Large courses with many sections
  - Unicode and special character handling
  - Complex markdown features
  - Error recovery and partial processing

## Running Tests

### Run All Tests
```bash
# Run all tests
uv run --extra dev pytest

# Or use the test runner
python run_tests.py
```

### Run Specific Test Categories
```bash
# Unit tests only
uv run --extra dev pytest tests/unit/ -v

# Integration tests only  
uv run --extra dev pytest tests/integration/ -v
```

### Run Specific Test Files
```bash
# Test URL conversion functionality
uv run --extra dev pytest tests/unit/test_url_conversion.py -v

# Test site generation
uv run --extra dev pytest tests/integration/test_site_generation.py -v
```

### Run Specific Test Methods
```bash
# Test specific functionality
uv run --extra dev pytest tests/unit/test_url_conversion.py::TestConvertPlainUrlsToLinks::test_preserve_urls_in_code_blocks -v
```

## Test Coverage

The test suite provides comprehensive coverage of:

### Core Functionality
- ✅ YAML frontmatter parsing (10 tests)
- ✅ URL detection and conversion (15 tests)
- ✅ Markdown processing (14 tests)
- ✅ Syntax highlighting (15 tests)
- ✅ Course metadata handling (8 tests)
- ✅ Template rendering (7 tests)
- ✅ Sorting and organization (8 tests)

### Integration Scenarios
- ✅ Complete site generation (4 tests)
- ✅ Large-scale processing (3 tests)
- ✅ Unicode and special characters (1 test)
- ✅ Complex markdown features (1 test)
- ✅ Error recovery (1 test)

### Edge Cases
- Empty files and directories
- Invalid YAML frontmatter
- Missing required fields
- Binary files in question directories
- Unicode characters and emojis
- Complex nested markdown structures
- Multiple courses and sections
- Large datasets (50+ questions)

## Key Test Features

### URL Detection Testing
The URL conversion tests ensure that:
- Plain text URLs are converted to clickable links
- URLs in code blocks remain untouched
- URLs in inline code are preserved
- Existing markdown links are not double-converted
- Trailing punctuation is handled correctly

### Error Handling
Tests verify graceful handling of:
- Invalid YAML frontmatter
- Missing required fields
- Non-existent files and directories
- Binary files in question directories
- Malformed markdown content

### Real-World Scenarios
Integration tests simulate:
- Large courses with 10+ sections and 50+ questions
- International content with unicode characters
- Complex markdown with tables, task lists, and code blocks
- Mixed valid/invalid content in the same course

## Adding New Tests

When adding new functionality to `generate_website.py`:

1. **Add unit tests** for new functions in appropriate `test_*.py` files
2. **Add integration tests** if the change affects the complete workflow
3. **Test edge cases** and error conditions
4. **Update this README** if new test categories are added

### Test Naming Convention
- Test files: `test_<functionality>.py`
- Test classes: `Test<ClassName>`
- Test methods: `test_<specific_behavior>`

### Example Test Structure
```python
class TestNewFeature:
    """Test the new feature functionality"""
    
    def test_basic_functionality(self):
        """Test basic feature behavior"""
        pass
        
    def test_edge_cases(self):
        """Test edge cases and error conditions"""
        pass
        
    def test_integration_with_existing_features(self):
        """Test how feature integrates with existing code"""
        pass
```

## Dependencies

The test suite requires:
- `pytest>=7.0.0` (defined in pyproject.toml dev dependencies)
- All main project dependencies for testing the actual functionality

## Configuration

Test configuration is defined in `pyproject.toml`:
- Test discovery paths
- Test file patterns
- Output formatting
- Custom markers for test categorization