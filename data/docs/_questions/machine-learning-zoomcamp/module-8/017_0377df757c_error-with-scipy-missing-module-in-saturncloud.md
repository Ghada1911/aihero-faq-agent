---
id: 0377df757c
question: Error with scipy missing module in SaturnCloud
sort_order: 17
---

I created a new environment in SaturnCloud and chose the image corresponding to Saturn with Tensorflow, but when I tried to fit the model it showed an error about the missing module: `scipy`.



1. Install the module in a new cell:
   
   ```bash
   !pip install scipy
   ```

2. Restart the kernel and fit the model again.