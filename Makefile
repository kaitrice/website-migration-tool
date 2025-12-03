dev:
	py -m src/tool.cli

test:
	pylint src && pytest

deploy: test
	git add .
	git commit -m "Automated deploy: $(MSG)"
	git push
