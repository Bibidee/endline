"use client";
import {useState} from "react";
export function CopyButton({value,label="Copy"}:{value:string;label?:string}){const [copied,setCopied]=useState(false);async function copy(){await navigator.clipboard?.writeText(value);setCopied(true);window.setTimeout(()=>setCopied(false),1400)}return <button className="copy-button" onClick={copy} title={`${label}: ${value}`} aria-label={label}>{copied?"Copied":"Copy"}</button>}
