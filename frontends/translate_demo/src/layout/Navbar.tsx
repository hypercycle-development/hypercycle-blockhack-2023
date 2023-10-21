import React from 'react';

const Navbar = () => {
    return (
        <>
     <nav className="border-b border-gray-700 bg-gray-950">
                <div className="max-w-screen-2xl flex flex-wrap items-center justify-between mx-auto px-4 py-4">
                    <div className="flex items-center">
                        <img src="https://static.wixstatic.com/media/f8ff07_d2a80c8471a543fe957466713cd4f14f~mv2.png/v1/fill/w_131,h_131,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Todalarity-Logo-2022_icon%20white.png" alt="Todalarity-Logo-2022_icon white.png" className="w-8 h-8 mr-2 object-cover object-center" />
                        <span className="self-center text-2xl font-semibold whitespace-nowrap">HyperCycle Client</span>
                    </div>
                </div>
            </nav>        </>
    );
};

export default Navbar;
