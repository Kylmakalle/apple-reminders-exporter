all: save organize

.PHONY: save
save:
	mkdir -p reminders
	shortcuts run "Export Reminders" -i ./reminders

.PHONY: organize
organize: 
	python3 scripts/organize.py ./reminders

.PHONY: clean
clean:
	rm -rf ./reminders