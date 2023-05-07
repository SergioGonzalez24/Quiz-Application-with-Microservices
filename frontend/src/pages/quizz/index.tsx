import { useRouter } from 'next/router';

export default function quizz() {
  const router = useRouter();
  const value = router.query.value;

  return (
    <div className="text-center">
      <h1 className="text-2xl font-bold mt-4">The value received is:</h1>
      <p className="text-4xl font-bold mt-4">{value}</p>
    </div>
  );
}
