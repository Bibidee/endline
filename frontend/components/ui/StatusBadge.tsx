export type LifecycleStatus="ACTIVE"|"DEPRECATED"|"SECURITY_ONLY"|"END_OF_LIFE"|"REPLACED"|"UNKNOWN"|string;
export const statusLabel=(status:LifecycleStatus)=>status.replaceAll("_"," ");
export function StatusBadge({status,compact=false}:{status:LifecycleStatus;compact?:boolean}){return <span className={`status-badge status-${status.toLowerCase()}${compact?" compact":""}`}><i aria-hidden="true"/>{statusLabel(status)}</span>}
export function FreshnessBadge({stale}:{stale?:boolean}){return <span className={`freshness-badge ${stale?"freshness-stale":"freshness-fresh"}`}>{stale?"Assessment stale":"Assessment current"}</span>}
