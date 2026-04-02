export default function PlayerInput({ setHoverText }) {
  return (
    <div
      className="player-input"
      onMouseEnter={() => setHoverText("Player input area")}
      onMouseLeave={() => setHoverText(null)}
    >
      <h3>Player Input</h3>
      <input type="text" placeholder="Type a command..." />
    </div>
  );
}
