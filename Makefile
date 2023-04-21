python-dev:
	cd python-server && make compile
	cd python-server && make python-build
	cd python-server && make run

rust-dev:	
	cd rust-server && cargo build
	cd rust-server && cargo run --bin cli