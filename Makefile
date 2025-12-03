dev:
	py -m tool.cli

test:
	pylint . && pytest

deploy: test
	git add .
	git commit -m "Automated deploy: $(MSG)"
	git push
