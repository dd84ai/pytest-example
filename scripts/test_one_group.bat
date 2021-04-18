cd ..
cmd /k "cd /d venv\Scripts & activate & cd /d    ..\.. & pytest -k ""test_"" test\${1}"