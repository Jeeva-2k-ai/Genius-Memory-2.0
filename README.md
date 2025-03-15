<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Genius Memory 2.0 Game</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Roboto', sans-serif;
      background-color: #f4f4f9;
      margin: 0;
      padding: 0;
      color: #333;
    }
    header {
      background-color: #5c6bc0;
      color: white;
      padding: 20px 0;
      text-align: center;
    }
    header h1 {
      margin: 0;
      font-size: 36px;
    }
    .container {
      max-width: 1000px;
      margin: 20px auto;
      padding: 20px;
      background-color: white;
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h2 {
      color: #5c6bc0;
      font-size: 28px;
      margin-top: 30px;
    }
    h3 {
      color: #1976d2;
      font-size: 24px;
      margin-top: 20px;
    }
    ul {
      list-style-type: none;
      padding-left: 0;
    }
    li {
      margin: 10px 0;
      font-size: 18px;
    }
    .icon {
      margin-right: 10px;
      font-size: 20px;
      color: #1976d2;
    }
    .content {
      padding: 10px;
      background-color: #f9f9f9;
      margin-top: 10px;
      border-radius: 5px;
    }
    .technologies {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
      gap: 10px;
    }
    .tech-item {
      padding: 10px;
      background-color: #e8eaf6;
      text-align: center;
      border-radius: 5px;
    }
    footer {
      text-align: center;
      padding: 20px;
      background-color: #5c6bc0;
      color: white;
      position: fixed;
      bottom: 0;
      width: 100%;
    }
  </style>
</head>
<body>

  <header>
    <h1>Genius Memory 2.0 Game 🧠🎮</h1>
    <p>Challenge your memory, logic, and coding skills with a collection of brain-training mini-games!</p>
  </header>

  <div class="container">
    <section>
      <h2>Game Overview 🎮</h2>
      <ul>
        <li><span class="icon">🖥️</span><strong>Syntax Sprint</strong> - Identify correct or incorrect syntax from a list of code snippets.</li>
        <li><span class="icon">🧠</span><strong>Trivia Lab</strong> - Answer trivia questions from various topics like science, history, and more.</li>
        <li><span class="icon">🔒</span><strong>Code Breakers</strong> - Decode hidden messages by solving programming and cryptography puzzles.</li>
        <li><span class="icon">🔢</span><strong>Digit Duel</strong> - Solve math puzzles and equations within a time limit.</li>
        <li><span class="icon">💻</span><strong>Byte Busters</strong> - Find and highlight programming-related words in a grid.</li>
        <li><span class="icon">🖼️</span><strong>Code Pixel</strong> - Choose the correct logo from available options based on the description.</li>
      </ul>
    </section>

    <section>
      <h2>How to Play 🕹️</h2>
      <div class="content">
        <p>Here’s how to play each of the mini-games in Genius Memory 2.0:</p>
        <ul>
          <li><strong>Syntax Sprint:</strong> Quickly identify the correct syntax to earn points before time runs out.</li>
          <li><strong>Trivia Lab:</strong> Answer trivia questions correctly to gain points. Each correct answer brings you closer to victory!</li>
          <li><strong>Code Breakers:</strong> Solve cryptography puzzles and uncover secret messages.</li>
          <li><strong>Digit Duel:</strong> Race against the clock and solve math problems faster than your opponent.</li>
          <li><strong>Byte Busters:</strong> Find programming-related words in a word search grid.</li>
          <li><strong>Code Pixel:</strong> Identify the correct logo based on the given prompt to score points.</li>
        </ul>
      </div>
    </section>

    <section>
      <h2>Technologies Used 💻</h2>
      <div class="technologies">
        <div class="tech-item">
          <p>🐍 <strong>Python</strong></p>
          <p>The primary language for backend operations and game logic.</p>
        </div>
        <div class="tech-item">
          <p>🕸️ <strong>Django</strong></p>
          <p>A high-level Python web framework for building and managing the game’s web application.</p>
        </div>
        <div class="tech-item">
          <p>📝 <strong>HTML</strong></p>
          <p>For structuring the web pages and content.</p>
        </div>
        <div class="tech-item">
          <p>🎨 <strong>CSS</strong></p>
          <p>For styling and the layout of the game interface.</p>
        </div>
        <div class="tech-item">
          <p>⚡ <strong>JavaScript</strong></p>
          <p>For interactive elements and game logic.</p>
        </div>
        <div class="tech-item">
          <p>📱 <strong>Bootstrap</strong></p>
          <p>For responsive design and mobile optimization.</p>
        </div>
        <div class="tech-item">
          <p>🧨 <strong>SweetAlert</strong></p>
          <p>For enhanced alert messages and notifications in the game.</p>
        </div>
        <div class="tech-item">
          <p>📊 <strong>SQLite</strong></p>
          <p>For storing game data such as high scores and user progress.</p>
        </div>
      </div>
    </section>
  </div>

  <footer>
    <p>&copy; 2025 Genius Memory 2.0. All Rights Reserved.</p>
  </footer>

</body>
</html>
