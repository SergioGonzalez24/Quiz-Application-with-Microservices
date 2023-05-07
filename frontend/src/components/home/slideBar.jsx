import { useState } from 'react';
import { useRouter } from 'next/router';

export default function SlideBar() {
  const [value, setValue] = useState(1);
  const router = useRouter();

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  const handleSubmit = () => {
    router.push(`/quizz?value=${value}`);
  };

  return (
    <div className="w-1/2 mx-auto">
      <input
        className="appearance-none w-full h-2 rounded-full bg-gray-300 outline-none"
        type="range"
        min="1"
        max="10"
        step="1"
        value={value}
        onChange={handleChange}
      />
      <div className="flex justify-between">
        <span>1</span>
        <span>10</span>
      </div>
      <p className="text-center text-2xl font-bold mt-4">{value}</p>
      <button
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4"
        onClick={handleSubmit}
      >
        Go to other page
      </button>
    </div>
  );
}
