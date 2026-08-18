import SpecimenTest.V143EFull
import Specimen.ArbitrarySizedSuchThat

open Lambda

#synth ArbitrarySizedSuchThat V143EExpr (fun e => V143EHasType ([] : List LMonoTy) e LMonoTy.bool)
