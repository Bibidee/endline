"use client";

import {useState} from "react";
import {useRouter} from "next/navigation";
import {connectWallet} from "../../lib/wallet";
import {contractAddress, getDependency, getDependencyCount, getSourceSet, submitRegistration} from "../../lib/genlayer";
import {validateSources} from "../../lib/validation";

const kinds=["API","SDK","MODEL","PACKAGE","PROTOCOL","SERVICE","OTHER"];

export default function Register(){
  const router=useRouter();
  const [sources,setSources]=useState([""]);
  const [message,setMessage]=useState("");
  const [submitting,setSubmitting]=useState(false);
  async function submit(e:React.FormEvent<HTMLFormElement>){
    e.preventDefault();
    const data=new FormData(e.currentTarget);
    const configured=sources.filter(Boolean);
    if(!contractAddress)return setMessage("CONFIGURATION REQUIRED: set NEXT_PUBLIC_ENDLINE_CONTRACT.");
    if(!validateSources(configured))return setMessage("Every source must be a public HTTPS URL (one to three, in order).");
    try{
      setSubmitting(true);
      const before=await getDependencyCount();
      if(before===null)throw new Error("RECONCILIATION ERROR: contract read unavailable");
      const account=await connectWallet();
      setMessage("WAITING FOR FINALITY…");
      const tx=await submitRegistration(account as `0x${string}`,[String(data.get("name")),String(data.get("kind")),String(data.get("version")),String(data.get("key")),configured[0],configured[1]||"",configured[2]||""]);
      const id=before+1;
      const [count,dependency,sourceSet]=await Promise.all([getDependencyCount(),getDependency(id),getSourceSet(id,1)]);
      if(count!==id||!dependency||!sourceSet||dependency.id!==id||dependency.canonical_key!==String(data.get("key"))||dependency.source_version!==1||dependency.assessment_count!==0||JSON.stringify(dependency.source_urls)!==JSON.stringify(configured)||JSON.stringify(sourceSet.source_urls)!==JSON.stringify(configured))throw new Error("RECONCILIATION ERROR: registration readback mismatch");
      setMessage(`SUCCESS — ${tx}`);
      router.push(`/d/${id}`);
    }catch(err){setMessage(err instanceof Error?err.message:"Wallet rejected transaction");}
    finally{setSubmitting(false);}
  }
  return <main><div className="rule">ENDLINE / REGISTRATION / STUDIONET 61999</div><h1>Register dependency</h1><p className="lede">Sources are configured by the registrant; ENDLINE does not certify their ownership.</p><form onSubmit={submit}><label>Name<input name="name" maxLength={120} required/></label><label>Kind<select name="kind">{kinds.map(x=><option key={x}>{x}</option>)}</select></label><label>Tracked version<input name="version" maxLength={80} required/></label><label>Canonical key<input name="key" pattern="[a-z0-9:._-]+" maxLength={180} required/><small>Example: example-sdk:python:4.x</small></label>{sources.map((s,i)=><label key={i}>SOURCE / {String(i+1).padStart(2,"0")}<input type="url" required value={s} onChange={e=>setSources(sources.map((v,j)=>j===i?e.target.value:v))}/></label>)}{sources.length<3&&<button type="button" onClick={()=>setSources([...sources,""])}>ADD SOURCE</button>}<p><button className="primary" disabled={submitting}>{submitting?"FINALISING…":"REGISTER DEPENDENCY"}</button></p>{message&&<p className={message.includes("SUCCESS")?"":"error"}>{message}</p>}</form></main>;
}
