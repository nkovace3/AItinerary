export function AmbientGlow() {
  return (
    <div className="pointer-events-none absolute inset-0 -z-10">
      <div className="absolute -top-24 -left-24 size-72 rounded-full bg-primary/30 blur-3xl" />
      <div className="absolute -right-24 -bottom-24 size-72 rounded-full bg-primary/20 blur-3xl" />
    </div>
  );
}
