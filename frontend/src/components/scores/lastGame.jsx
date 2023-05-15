export default function LastGame() {
    return (
      <div className="lastGame bg-gray-100 py-6 px-4 rounded-lg">
  
        <h1 className="lastGame_score text-4xl font-bold text-center text-gray-800 mb-4">
          78  pts
        </h1>
  
        <button className="lastGame_button block mx-auto py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-yellow-500 hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-yellow-400">
          Jugar de nuevo
        </button>
      </div>
    );
  }