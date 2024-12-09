test: 
	python -m pytest

push:
	git add .
	git commit -m "update"
	git push origin main


.PHONY : test push