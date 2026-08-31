# ENDLINE Release Evidence

Repository: https://github.com/Bibidee/endline
Branch: master
Source commit: 2cef55d64abec33cdc6a21b6b12efc882b83b75d
Contract SHA-256: 1BB6D7DBE96DD25B450F347BEAA67EA5BE08D8C9A298EA8B5F098A52CD89167B
Runtime Depends: py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6

Contract gates: lint PASS; validate PASS; schema PASS (9 methods); typecheck PASS.
Policy tests: 64 passed. Direct Mode: blocked by Windows gltest temp-file lock; CI executes the suite on Ubuntu.
Frontend: typecheck PASS; build PASS; local Vitest blocked by OneDrive resolver.
GitHub Actions: run 33431297655 in progress at last check.

Studionet contract: 0xAC619CE31aD990C77b988308Ab101282FE75A22E
Deployment tx: 0xd4cd8cac1af337ea3aafc21d04b600dd48dce66d7fa1120353135e9cf3913b72
Schema lookup: verified.
Lifecycle transactions (all FINALIZED, MAJORITY_AGREE, execution SUCCESS):

- Registration: `0x3b9dac2cc9d81af034cbd35da31e2b016d9bcc2265c7eb15da217ffed0afa82f`
- Assessment 1: `0x9ab09a404536d88c5c43a13cd5a8fd82c33963d495a8a163f5d1e7ffb9621da0`
- Source update: `0x0495135638d84bf9251faeeb3f263d25988d6213049c42073c98447c0ca670bb`
- Assessment 2: `0xb8c2034bca0d9216837a380ee4836c2a32e58deb4f2ee6fc0f2c79838566ce31`

Authoritative readback: dependency `1` has `source_version=2`, `assessment_count=2`, `current_assessment_sequence=2`, `current_assessment_source_version=2`, and `is_stale=false`. SourceSet 1 remains readable and Assessment 1 references source version 1; SourceSet 2 exists and Assessment 2 references source version 2.
Frontend deployment: not available.
