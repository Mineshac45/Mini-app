<html>
<head>
    <title>Mines_Hack_24HR</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <style>
        body {
            background-color: black; /* Set the background color to black */
            font-family: 'Arial', sans-serif;
        }
        .grid-item {
            width: 120px; /* Adjusted width to make grid smaller */
            height: 80px; /* Adjusted height to make grid smaller */
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .star-cell {
            background-color: #f39c12; /* Yellow-orange background for the star cells */
            border-radius: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }
        .star-icon {
            font-size: 60px; /* Slightly smaller star icon */
            color: #fff; /* White color */
        }
        .blue-cell {
            background-color: #1e3a8a; /* Tailwind Blue-900 background color */
            border-radius: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }
        .blue-dot {
            width: 40px; /* Smaller size for the blue dots */
            height: 40px;
            background: linear-gradient(to right, #3b82f6, #1d4ed8); /* Gradient from blue-500 to blue-700 */
            border-radius: 50%;
        }
        /* Increase size of the title */
        h1 {
            font-size: 5.2rem; /* Larger title size */
        }
        /* Make the slider and button bigger */
        .slider {
            width: 80%;
            height: 40px; /* Increased height */
        }
        .slider::-webkit-slider-thumb {
            width: 30px; /* Increased width of slider thumb */
            height: 30px; /* Increased height of slider thumb */
        }
        #signalButton {
            padding: 32px 64px; /* Increased padding */
            font-size: 3.2rem; /* Larger font size */
        }
    </style>
</head>
<body class="flex flex-col items-center justify-center min-h-screen text-white">
    <div class="text-center">
        <h1 class="text-2xl font-bold mb-4 text-yellow-500">Mines Hack 24HR</h1>
        <div class="bg-blue-500 p-4 rounded-lg shadow-lg" style="border: 5px solid #FFD700;">
            <!-- Game Grid -->
            <div id="gameGrid" class="grid grid-cols-5 gap-4 justify-center">
                <!-- Cells will be generated dynamically with JavaScript -->
            </div>
        </div>
        <div class="mt-8">
            <h2 class="text-3x1 font-bold mb-2">NUMBER OF MINES</h2>
            <div class="flex items-center justify-center mb-4">
                <input id="mineSlider" type="range" min="1" max="10" value="3" class="slider">
                <span id="mineCount" class="ml-4 text-2xl font-bold">3</span>
            </div>
            <button id="signalButton" class="bg-blue-700 text-white font-bold py-2 px-8 rounded-lg">GET SIGNAL</button>
        </div>
    </div>

    <script>
        // Initialize variables
        const grid = document.getElementById('gameGrid');
        const slider = document.getElementById('mineSlider');
        const mineCountDisplay = document.getElementById('mineCount');
        const signalButton = document.getElementById('signalButton');
        const gridSize = 25; // 5x5 grid
        let numMines = parseInt(slider.value);

        // Function to update the grid based on the number of mines
        function updateGrid() {
            // Clear existing grid content
            grid.innerHTML = '';

            // Determine the number of stars to show based on the slider value
            const maxStars = 12; // Maximum prediction for 1 mine
            const minStars = 5; // Minimum prediction for 10 mines
            const starsToShow = maxStars - Math.floor(((numMines - 1) / 9) * (maxStars - minStars));

            // Create empty grid
            const cells = Array(gridSize).fill('dot');

            // Randomly select positions for stars
            const starPositions = new Set();
            while (starPositions.size < starsToShow) {
                const randomPos = Math.floor(Math.random() * gridSize);
                starPositions.add(randomPos);
            }

            // Update grid content based on star positions
            for (let i = 0; i < gridSize; i++) {
                const cell = document.createElement('div');
                cell.classList.add('grid-item', 'rounded', 'flex', 'items-center', 'justify-center');

                if (starPositions.has(i)) {
                    // If it's a star position, use the star cell style
                    cell.classList.add('star-cell');
                    const starIcon = document.createElement('i');
                    starIcon.classList.add('fas', 'fa-star', 'star-icon');
                    cell.appendChild(starIcon);
                } else {
                    // Regular dot with the new blue cell design
                    cell.classList.add('blue-cell');
                    const blueDot = document.createElement('div');
                    blueDot.classList.add('blue-dot');
                    cell.appendChild(blueDot);
                }

                // Add cell to grid
                grid.appendChild(cell);
            }
        }

        // Update the displayed mine count when the slider is changed
        slider.addEventListener('input', () => {
            numMines = parseInt(slider.value);
            mineCountDisplay.textContent = numMines;
        });

        // Button click event to generate a new signal
        signalButton.addEventListener('click', updateGrid);

        // Initial grid setup
        updateGrid();
    </script>
</body>
</html>

