# Contributing to Park FastPass API

## 🎯 Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/park-fastpass-api.git`
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Commit: `git commit -am 'Add some feature'`
6. Push: `git push origin feature/your-feature-name`
7. Open a Pull Request

## 📋 Development Setup

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
cd backend
pip install -r requirements.txt

# Start development server
python app/main.py
```

## 🧪 Testing

```bash
cd backend
pytest
```

## 📝 Code Style

- Follow PEP 8
- Use type hints
- Add docstrings to functions
- Keep lines under 100 characters

## 🐛 Bug Reports

Include:
- Python version
- OS
- Steps to reproduce
- Expected vs actual behavior
- Error messages/logs

## ✨ Feature Requests

Describe:
- Use case
- Proposed solution
- Alternatives considered
- Additional context

## 📚 Documentation

Update docs when:
- Adding new endpoints
- Changing configuration
- Updating dependencies
- Fixing bugs with workarounds

## 🚀 Release Process

1. Update version in `main.py`
2. Update `CHANGELOG.md`
3. Create release on GitHub
4. Deploy to production

---

**Thank you for contributing! 🎉**
