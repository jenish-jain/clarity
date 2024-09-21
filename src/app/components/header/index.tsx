"use client";

import React from "react";
import Box from "@mui/joy/Box";

type HeaderProps = {
  sticky: boolean;
  showDrawer: boolean;
};

export const Header: React.FC<HeaderProps> = ({
}) => {
  return (
    <header>
       <Box
       className="poppins-extrabold"
       sx={{ display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '9vh' }}>
        <h1 >Clarity</h1>
       </Box>
    </header>
  );
};
