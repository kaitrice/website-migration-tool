dev:
	py -m tool.cli

test:
	pylint . && pytest

deploy: test
	git add .
	git commit -m "deploy: automated"
	git push
