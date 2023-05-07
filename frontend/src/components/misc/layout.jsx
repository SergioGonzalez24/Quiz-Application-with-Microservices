import navbar from "./navbar";
export default function Layout({ children }) {
  return (
    <>
      <navbar />
      <main>{ children }</main>
    </>
  );
}
