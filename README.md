## Binary-Pattern-Rectangle-Counter

This Python project implements an algorithm to detect and count the number of rectangles within a 2D binary pattern. Developed as part of the CENG 111 course at METU.

- Identifies valid rectangles defined by "1" borders that contain at least one "0" inside.

- The algorithm is designed to count nested and overlapping rectangles as distinct entities.

- Developed from scratch without importing any external libraries, utilizing nested iterative searches to validate geometric properties.

**Logic Overview**

The system traverses a list of strings (representing the 2D grid) to find potential top-left corners of rectangles and then validates every possible bottom-right coordinate to ensure border integrity and empty interiors.
