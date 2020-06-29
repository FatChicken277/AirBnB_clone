#!/usr/bin/env bash
set -e

{
	cat <<- 'EOH'
		# how AUTHORS it is generated, see `generate-authors.sh`.
	EOH
	echo
	git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS

sed -i '/github.com/d' AUTHORS
