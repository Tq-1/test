.PHONY: validate test check

validate:
	python skills/traceable-research/scripts/validate_skill.py .

test:
	python -m unittest discover -s tests -v

check: validate test
