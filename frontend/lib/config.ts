export const network={chainId:61999,chainHex:"0xf22f",chainName:"GenLayer Studionet",rpcUrls:[process.env.NEXT_PUBLIC_GENLAYER_RPC||"https://studio.genlayer.com/api"],nativeCurrency:{name:"GEN",symbol:"GEN",decimals:18},blockExplorerUrls:["https://explorer-studio.genlayer.com"]};
export const contractAddress=process.env.NEXT_PUBLIC_ENDLINE_CONTRACT as `0x${string}`|undefined;
