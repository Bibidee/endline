import {createClient} from "genlayer-js";
import {studionet} from "genlayer-js/chains";
import {TransactionStatus} from "genlayer-js/types";
import {contractAddress} from "./config";
export type Dependency={id:number;creator:string;name:string;kind:string;tracked_version:string;canonical_key:string;source_urls:string[];source_version:number;current_assessment_source_version?:number;current_assessment_sequence?:number;current_assessed_at?:string;current_status:string;current_effective_date:string;current_replacement:string;current_migration_required:boolean;current_breaking_change:boolean;current_reason_code:string;assessment_count:number;is_stale?:boolean};
export type Assessment={dependency_id:number;sequence:number;requested_by:string;source_version:number;assessed_at:string;status:string;effective_date:string;replacement:string;migration_required:boolean;breaking_change:boolean;reason_code:string;evidence_state:string;summary:string};
export type SourceSet={dependency_id:number;version:number;source_urls:string[];created_at:string};
export const readClient=()=>createClient({chain:studionet});
export const writeClient=(address:`0x${string}`)=>createClient({chain:studionet,account:address,provider:window.ethereum});
export {TransactionStatus,contractAddress};
export type FinalityReceipt={statusName?:string;resultName?:string;txExecutionResultName?:string};
export function transactionSucceeded(receipt:FinalityReceipt){return receipt.statusName==="FINALIZED"&&receipt.resultName==="MAJORITY_AGREE"&&receipt.txExecutionResultName==="FINISHED_WITH_RETURN"}
export function transactionErrorMessage(error:unknown){if(error&&typeof error==="object"){const value=error as {code?:number;message?:unknown;shortMessage?:unknown;details?:unknown};if(value.code===4001)return "Wallet rejected transaction";for(const candidate of [value.shortMessage,value.message,value.details])if(typeof candidate==="string"&&candidate.trim())return candidate}return "Transaction could not be submitted. Check the wallet network and available GEN, then try again."}
export async function listDependencies(){if(!contractAddress)return null;return await readClient().readContract({address:contractAddress,functionName:"get_dependencies",args:[0,50]}) as unknown as Dependency[]}
export async function getDependencyCount(){if(!contractAddress)return null;return Number(await readClient().readContract({address:contractAddress,functionName:"get_dependency_count",args:[]}))}
export async function getDependency(id:number){if(!contractAddress)return null;return await readClient().readContract({address:contractAddress,functionName:"get_dependency",args:[id]}) as unknown as Dependency}
export async function getAssessments(id:number){if(!contractAddress)return null;return await readClient().readContract({address:contractAddress,functionName:"get_assessments",args:[id,0,32]}) as unknown as Assessment[]}
export async function getSourceSet(id:number,version:number){if(!contractAddress)return null;return await readClient().readContract({address:contractAddress,functionName:"get_source_set",args:[id,version]}) as unknown as SourceSet}
async function send(address:`0x${string}`,functionName:string,args:unknown[]){const c=writeClient(address);const hash=await c.writeContract({address:contractAddress!,functionName,args:args as any,value:BigInt(0)});const receipt=await readClient().waitForTransactionReceipt({hash,status:TransactionStatus.FINALIZED});if(!transactionSucceeded(receipt))throw new Error("Finalised transaction did not execute successfully");return hash}
export async function submitRegistration(address:`0x${string}`,args:[string,string,string,string,string,string,string]){return send(address,"register_dependency",args)}
export async function submitAssessment(address:`0x${string}`,id:number){return send(address,"assess_dependency",[id])}
export async function submitSourceUpdate(address:`0x${string}`,id:number,sources:[string,string,string]){return send(address,"update_sources",[id,...sources])}
