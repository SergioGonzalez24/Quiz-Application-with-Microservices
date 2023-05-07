import "@/styles/globals.css";
import type { AppProps } from "next/app";
import { Layout } from "@/components/misc";
import Head from "next/head";



export default function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>Quizz App</title>
      </Head>
      <Layout>
        <Component {...pageProps} />
      </Layout>
    </>
  );
}
