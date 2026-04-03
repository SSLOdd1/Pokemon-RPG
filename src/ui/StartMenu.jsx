import React from "react";

function StartMenu({
	onNewGame = () => {},
	onLoadGame = () => {},
	onOptions = () => {},
	onQuit = () => {},
}) {
	return (
		<div style={styles.container}>
			<h1 style={styles.title}>Pokémon RPG</h1>
			<div style={styles.menu}>
				<button style={styles.button} onClick={onNewGame}>
					New Game
				</button>
				<button style={styles.button} onClick={onLoadGame}>
					Load Saved Games
				</button>
				<button style={styles.button} onClick={onOptions}>
					Options
				</button>
				<button style={styles.button} onClick={onQuit}>
					Quit
				</button>
			</div>
		</div>
	);
}

const styles = {
	container: {
		minHeight: "100vh",
		display: "flex",
		flexDirection: "column",
		alignItems: "center",
		justifyContent: "center",
		background: "#f5f7fb",
		gap: "1.5rem",
	},
	title: {
		margin: 0,
		fontSize: "2rem",
		color: "#1f2937",
	},
	menu: {
		display: "flex",
		flexDirection: "column",
		gap: "0.75rem",
		width: "260px",
	},
	button: {
		padding: "0.75rem 1rem",
		fontSize: "1rem",
		borderRadius: "8px",
		border: "1px solid #d1d5db",
		background: "#ffffff",
		cursor: "pointer",
	},
};

export default StartMenu;
