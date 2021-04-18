cd ..
cmd /k "cd /d venv\Scripts & activate & cd /d    ..\.. & pytest -k ""test_"" test\code & pytest -k ""test_search_real_find"" test\requests"