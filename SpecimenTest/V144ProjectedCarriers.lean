import Specimen.DeriveConstrainedProducer
import Plausible.Arbitrary

open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

inductive V144Ty : Type where
  | atom
  | arrow (a b : V144Ty)
  deriving Repr, BEq

instance : Arbitrary V144Ty where
  arbitrary := pure .atom

structure V144Base : Type 1 where
  Metadata : Type
  IDMeta : Type

structure V144ParamsT : Type 1 where
  base : V144Base
  TypeType : Type

structure V144Identifier (M : Type) : Type where
  metadata : M

deriving instance Arbitrary for V144Identifier

abbrev V144Base0 : V144Base := ⟨Unit, Unit⟩
abbrev V144Mono (b : V144Base) : V144ParamsT := ⟨b, V144Ty⟩
abbrev V144P0 : V144ParamsT := V144Mono V144Base0

namespace V144Meta
inductive Expr (p : V144ParamsT) : Type where
  | lit (m : p.base.Metadata)
  | rec (m : p.base.Metadata) (body : Expr p)
inductive HasType : Expr V144P0 → V144Ty → Prop where
  | lit : HasType (.lit ()) .atom
  | rec : HasType body τ → HasType (.rec () body) τ
#guard_msgs(drop info, drop warning) in
derive_mutual (fun τ => ∃ e : Expr V144P0, HasType e τ)
end V144Meta

namespace V144IDDirect
inductive Expr (p : V144ParamsT) : Type where
  | lit (m : p.base.Metadata)
  | rec (m : p.base.Metadata) (id : p.base.IDMeta) (body : Expr p)
inductive HasType : Expr V144P0 → V144Ty → Prop where
  | lit : HasType (.lit ()) .atom
  | rec : HasType body τ → HasType (.rec () () body) τ
#guard_msgs(drop info, drop warning) in
derive_mutual (fun τ => ∃ e : Expr V144P0, HasType e τ)
end V144IDDirect

namespace V144TypeAnn
inductive Expr (p : V144ParamsT) : Type where
  | lit (m : p.base.Metadata)
  | rec (m : p.base.Metadata) (ann : Option p.TypeType) (body : Expr p)
inductive HasType : Expr V144P0 → V144Ty → Prop where
  | lit : HasType (.lit ()) .atom
  | rec : HasType body τ → HasType (.rec () (some τ) body) τ
#guard_msgs(drop info, drop warning) in
derive_mutual (fun τ => ∃ e : Expr V144P0, HasType e τ)
end V144TypeAnn

namespace V144IdentifierNested
inductive Expr (p : V144ParamsT) : Type where
  | lit (m : p.base.Metadata)
  | rec (m : p.base.Metadata) (id : V144Identifier p.base.IDMeta) (body : Expr p)
inductive HasType : Expr V144P0 → V144Ty → Prop where
  | lit : HasType (.lit ()) .atom
  | rec : HasType body τ → HasType (.rec () ⟨()⟩ body) τ
#guard_msgs(drop info, drop warning) in
derive_mutual (fun τ => ∃ e : Expr V144P0, HasType e τ)
end V144IdentifierNested

namespace V144All
inductive Expr (p : V144ParamsT) : Type where
  | lit (m : p.base.Metadata)
  | rec (m : p.base.Metadata)
        (id : V144Identifier p.base.IDMeta)
        (ann : Option p.TypeType)
        (body : Expr p)
inductive HasType : Expr V144P0 → V144Ty → Prop where
  | lit : HasType (.lit ()) .atom
  | rec : HasType body τ → HasType (.rec () ⟨()⟩ (some τ) body) τ
#guard_msgs(drop info, drop warning) in
derive_mutual (fun τ => ∃ e : Expr V144P0, HasType e τ)
end V144All
