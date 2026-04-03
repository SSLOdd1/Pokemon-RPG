export default function PlayerInput({ setHoverText }) {
  return (
    <div
      className="player-input"
    >
      <h3>Player Input</h3>
       <ul className="main-menu-options">
          <li><span className="menu-key">1</span><span className="menu-label">Explore</span></li>
          <li><span className="menu-key">2</span><span className="menu-label">Inventory</span></li>
          <li><span className="menu-key">3</span><span className="menu-label">Quests</span></li>
          <li><span className="menu-key">4</span><span className="menu-label">Talk to characters</span></li>
          <li><span className="menu-key">5</span><span className="menu-label">Fight</span></li>
          <li><span className="menu-key">6</span><span className="menu-label">Perform for coin / Beg for coin</span></li>
          <li><span className="menu-key">9</span><span className="menu-label">Save Game</span></li>
          <li><span className="menu-key">0</span><span className="menu-label">Exit</span></li>
        </ul>
    </div>
  );
}
