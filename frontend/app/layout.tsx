import type { Metadata } from 'next';
import './globals.css';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

export const metadata: Metadata = {
  title: 'AI Credibility Engine',
  description: 'AI & Machine Learning Text Classification System using FastAPI and Next.js 15',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body className="bg-black text-zinc-100 min-h-screen flex flex-col antialiased">
        <Navbar />
        <main className="flex-grow max-w-7xl mx-auto px-6 py-8 w-full">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
