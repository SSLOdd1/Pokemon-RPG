import React from 'react';

export default function NewGame({ new_game }) {
  return (
    <button type="button" onClick={new_game}>
      New Game
    </button>
  );
}