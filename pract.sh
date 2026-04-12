#!/bin/bash
echo "deployment started: $(date)" >> deployment.log

echo "pulling latest code .."

if git pull origin master; then 
    echo "✅ Git pull successful"
    echo "✅ Git pull successful" >> deployment.log
else
    echo "❌ Git pull failed"
    echo "❌ Git pull failed" >> deployment.log
    exit 1
fi

echo "📦 Checking dependencies..."
if  [ -f requirement.txt ]; then
    echo "✅ File requirement.txt exists .."
else
    echo " ❌File requirement.txt does not exists .."
fi

echo "===================================="
echo "🎉 Deployment Completed Successfully!"
echo "===================================="