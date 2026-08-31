import {createClient} from "genlayer-js";
import {studionet} from "genlayer-js/chains";
import {TransactionStatus} from "genlayer-js/types";
import {contractAddress} from "./config";

export type Dependency = {id:number; creator:string; name:string; kind:string; tracked_version:string; canonical_key:string; source_urls:string[]; source_version:number; current_assessment_source_version?:number; current_assessment_sequence?:number; current_assessed_at?:number; current_status:string; current_effective_date:string; current_replacement:string; current_migration_required:boolean; current_breaking_change:boolean; current_reason_code:string; assessment_count:number};
export type Assessment = {dependency_id:number; sequence:number; requested_by:string; source_version:number; status:string; effective_date:string; replacement:string; migration_required:boolean; breaking_change:boolean; reason_code:string; evidence_state:string; summary:string};
export const readClient=()=>createClient({chain:studionet});
export const writeClient=(address:`0x${string}`)=>createClient({chain:studionet,account:address,provider:window.ethereum});
export {TransactionStatus,contractAddress};
export async function listDependencies(){if(!contractAddress)return null;return await readClient().readContract({address:contractAddress,functionName:"get_dependencies",args:[0,50]}) as unknown as Dependency[]}
export async function getDependency(id:number){if(!contractAddress)return null;return await readClient().readContract({address:contractAddress,functionName:"get_dependency",args:[id]}) as unknown as Dependency}
export async function getAssessments(id:number){if(!contractAddress)return null;return await readClient().readContract({address:contractAddress,functionName:"get_assessments",args:[id,0,32]}) as unknown as Assessment[]}
export async function submitRegistration(address:`0x${string}`,args:[string,string,string,string,string,string,string]){const c=writeClient(address);await c.connect("studionet");const hash=await c.writeContract({address:contractAddress!,functionName:"register_dependency",args,value:BigInt(0)});const receipt=await readClient().waitForTransactionReceipt({hash,status:TransactionStatus.FINALIZED});if(receipt.statusName!=="FINALIZED"||receipt.resultName!=="MAJORITY_AGREE")throw new Error("Transaction finalised without successful execution");return hash}
