import {describe, expect, it} from "vitest";
import {transactionSucceeded} from "./genlayer";

describe("transaction success policy", () => {
  const complete={statusName:"FINALIZED",resultName:"MAJORITY_AGREE",txExecutionResultName:"FINISHED_WITH_RETURN"};
  it("accepts only a finalised, agreed, successful execution",()=>expect(transactionSucceeded(complete)).toBe(true));
  it.each([
    {...complete,statusName:"PENDING"},
    {...complete,resultName:"MAJORITY_DISAGREE"},
    {...complete,txExecutionResultName:"REVERTED"},
    {statusName:"FINALIZED",resultName:"MAJORITY_AGREE"},
  ])("rejects an incomplete or unsuccessful receipt",receipt=>expect(transactionSucceeded(receipt)).toBe(false));
});
