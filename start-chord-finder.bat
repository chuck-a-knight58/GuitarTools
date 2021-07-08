set root=%~dp0
cd %root%
start "Temp Server" node server.js
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://localhost:8080/chords.html