import {describe, expect, it} from "vitest";
import {findAssessmentForVersion,findMatchingRegistration,transactionSucceeded} from "./genlayer";

describe("transaction success policy", () => {
  const complete={statusName:"FINALIZED",resultName:"MAJORITY_AGREE",txExecutionResultName:"FINISHED_WITH_RETURN"};
  it("accepts only a finalised, agreed, successful execution",()=>expect(transactionSucceeded(complete)).toBe(true));
  it("accepts Studionet receipts that omit the optional execution result",()=>expect(transactionSucceeded({statusName:"FINALIZED",resultName:"MAJORITY_AGREE"})).toBe(true));
  it.each([
    {...complete,statusName:"PENDING"},
    {...complete,resultName:"MAJORITY_DISAGREE"},
    {...complete,txExecutionResultName:"REVERTED"},
    {statusName:"FINALIZED",resultName:"MAJORITY_AGREE",txExecutionResultName:"FINISHED_WITH_ERROR"},
  ])("rejects an incomplete or unsuccessful receipt",receipt=>expect(transactionSucceeded(receipt)).toBe(false));
});
describe("concurrency-safe reconciliation",()=>{
  const dep=(id:number,creator:string,key:string):any=>({id,creator,canonical_key:key,source_version:1,assessment_count:0,source_urls:["https://a"]});
  it("finds the matching registration in a concurrent range",()=>expect(findMatchingRegistration([dep(2,"0xabc","k"),dep(3,"0xdef","k")],"0xdef","k",["https://a"]).id).toBe(3));
  it("rejects ambiguous registration matches",()=>expect(()=>findMatchingRegistration([dep(2,"0xabc","k"),dep(3,"0xabc","k")],"0xabc","k",["https://a"])).toThrow("ambiguous"));
  it("finds an assessment after the prior sequence for the expected source",()=>expect(findAssessmentForVersion([{sequence:3,source_version:2} as any],1,2)?.sequence).toBe(3));
});
