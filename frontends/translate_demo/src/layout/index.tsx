import Navbar from './Navbar';
import Footer from './Footer';
const Layout = ({ children }: any) => {
    return (
        <div className='bg-gray-950 text-gray-100'>
            <Navbar />
            <div className='w-full max-w-screen-2xl mx-auto'>
            {
                children
            }
            </div>
            <Footer />
        </div>
    );
};

export default Layout;