import SpecimenTest.V143EFull
import Specimen.ArbitrarySizedSuchThat
import Plausible.Gen

open Plausible
open Lambda

#eval show IO Unit from do
  let _e ← Gen.run
    (ArbitrarySizedSuchThat.arbitrarySizedST
      (fun e => V143EHasType ([] : List LMonoTy) e LMonoTy.bool) 4)
    3
  IO.println "V144_ONE_SAMPLE_OK"
