# Monty Hall Applet Call Tree

This describes the main call tree and entry points for the Monty Hall applet:

## Entry Points
- The main entry point for user interaction is the `clickDoor(index)` function.
- Event listeners are attached to the doors:
  - `door0` → `clickDoor(0)`
  - `door1` → `clickDoor(1)`
  - `door2` → `clickDoor(2)`

## Game Flow
1. **Page Load**
    - Variables are initialized.
    - Event listeners are set up.
    - `resetGame()` is called to initialize the game state and UI.

2. **resetGame()**
    - Resets game state and UI.
    - Calls `updateVars()`.
    - Calls `showMessage('Start the game')`.

3. **User clicks a door**
    - Triggers `clickDoor(index)`.

4. **clickDoor(index)**
    - If first click:
        - Sets `chosen`.
        - Marks the door.
        - Calls `updateVars()`.
        - Calls `showMessage('Let me open a door for you!')`.
        - After 2 seconds, opens an empty door and starts countdown.
        - Starts interval for countdown:
            - Each second: `showMessage('You can switch the next X seconds!')`
            - After countdown: opens chosen door, shows win/lose message, updates stats, calls `resetGame()` after 1.5s.
    - If second click (during countdown):
        - Switches `chosen`.
        - Opens chosen door, shows win/lose message, updates stats, calls `resetGame()` after 1.5s.

5. **Helper functions**
    - `showMessage(msg)` — updates the message area.
    - `updateVars()` — updates hidden variables.
    - `updateStats()` — updates win/game counters.

## Summary
- Entry point for user interaction: `clickDoor(index)` via door click event listeners.
- Game flow is managed by `clickDoor`, `resetGame`, and helper functions.
- All UI updates and game logic are handled inside these functions.
