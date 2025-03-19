import React from "react";

const Navbar = () => {
  return (
    <nav className="bg-white shadow-md py-4 px-6 flex justify-between items-center">
      <h1 className="text-xl font-bold text-blue-600">Athlete Edge</h1>
      <ul className="flex space-x-6">
        <li className="nav-link cursor-pointer text-gray-700 hover:text-blue-600">Home</li>
        <li className="nav-link cursor-pointer text-gray-700 hover:text-blue-600">Dashboard</li>
        <li className="nav-link cursor-pointer text-gray-700 hover:text-blue-600">Profile</li>
      </ul>
    </nav>
  );
};

export default Navbar;
