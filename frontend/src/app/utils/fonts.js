import {Poppins, Inter} from "next/font/google"

export const poppins_init = Poppins({
    subsets: ['latin'],
    display: 'swap',
    variable: '--font-poppins',
    weight: ['300', '500'],
    });     

export const inter_init = Inter({
    subsets: ['latin'],
    display: 'swap',
    variable: '--font-inter',
    weight: ['300', '500'],
    });  
export const poppins = poppins_init.variable
export const inter = inter_init.variable