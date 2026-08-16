from pathlib import Path

DERIVE = Path('Specimen/DeriveConstrainedProducer.lean')
EMIT = Path('Specimen/MakeConstrainedProducerInstance.lean')

# Patch only the fallback/mutual parts path. Earlier deriveConstrainedProducer and
# collectSpecDependencies remain unchanged by design.
s = DERIVE.read_text()
marker = 'def deriveConstrainedProducerParts\n'
pos = s.index(marker)
head, tail = s[:pos], s[pos:]
old = '''      if ident.isFVar then ident.fvarId!.getUserName
      else if let some outIdx := outputIdxs.findIdx? (· == i) then
        outputVars[outIdx]!.fvarId!.getUserName
      else throwError m!"{ident} is expected to be a variable.")'''
new = '''      if ident.isFVar then ident.fvarId!.getUserName
      else if ident.isConst then
        -- V147b K6_GLOBAL_FIXED_INPUT: preserve an actual global constant by
        -- its global name.  The emitter recognizes that name as global and
        -- deliberately does not quantify it as a producer parameter.
        ident.constName!
      else if let some outIdx := outputIdxs.findIdx? (· == i) then
        outputVars[outIdx]!.fvarId!.getUserName
      else throwError m!"{ident} is expected to be a variable.")'''
if tail.count(old) < 1:
    raise SystemExit('deriveConstrainedProducerParts target not found')
tail = tail.replace(old, new, 1)
DERIVE.write_text(head + tail)

s = EMIT.read_text()
marker = 'def mkConstrainedProducerMutualPieces\n'
pos = s.index(marker)
head, tail = s[:pos], s[pos:]
old1 = '''    for (paramName, paramType, paramTypeSyntax) in paramInfo do
      if paramType.isSort then
        typeParams := typeParams.push paramName
      if paramName ∉ targetVarsList then
        outerParams := outerParams.push (mkIdent paramName)
        paramTypes := paramTypes.push paramTypeSyntax
        if paramType.isSort then
          innerParamBinders := innerParamBinders.push (← `(($(mkIdent paramName) : Sort _)))
        else
          innerParamBinders := innerParamBinders.push (← `(($(mkIdent paramName) : $paramTypeSyntax)))
      else
        outputTypeSyntaxes := outputTypeSyntaxes.push paramTypeSyntax
'''
new1 = '''    for (paramName, paramType, paramTypeSyntax) in paramInfo do
      let isGlobalFixed ←
        try
          let _ ← getConstInfo paramName
          pure true
        catch _ => pure false
      -- V147b K6_GLOBAL_FIXED_INPUT: names that resolve to actual environment
      -- constants are fixed values, not lambda parameters.  Leaving them out
      -- of the generated binders lets emitted syntax resolve the same global.
      if !isGlobalFixed && paramType.isSort then
        typeParams := typeParams.push paramName
      if paramName ∉ targetVarsList && !isGlobalFixed then
        outerParams := outerParams.push (mkIdent paramName)
        paramTypes := paramTypes.push paramTypeSyntax
        if paramType.isSort then
          innerParamBinders := innerParamBinders.push (← `(($(mkIdent paramName) : Sort _)))
        else
          innerParamBinders := innerParamBinders.push (← `(($(mkIdent paramName) : $paramTypeSyntax)))
      else if paramName ∈ targetVarsList then
        outputTypeSyntaxes := outputTypeSyntaxes.push paramTypeSyntax
'''
if tail.count(old1) < 1:
    raise SystemExit('mutual emitter param loop target not found')
tail = tail.replace(old1, new1, 1)
old2 = '''    for (paramName, paramType, paramTypeSyntax) in paramInfo do
      if paramName ∉ targetVarsList then
        if paramType.isSort then
          allParamNamesAndTypes := allParamNamesAndTypes.push (mkIdent paramName, ← `(Sort _))
        else
          allParamNamesAndTypes := allParamNamesAndTypes.push (mkIdent paramName, paramTypeSyntax)
'''
new2 = '''    for (paramName, paramType, paramTypeSyntax) in paramInfo do
      let isGlobalFixed ←
        try
          let _ ← getConstInfo paramName
          pure true
        catch _ => pure false
      if paramName ∉ targetVarsList && !isGlobalFixed then
        if paramType.isSort then
          allParamNamesAndTypes := allParamNamesAndTypes.push (mkIdent paramName, ← `(Sort _))
        else
          allParamNamesAndTypes := allParamNamesAndTypes.push (mkIdent paramName, paramTypeSyntax)
'''
if tail.count(old2) < 1:
    raise SystemExit('mutual emitter full type loop target not found')
tail = tail.replace(old2, new2, 1)
EMIT.write_text(head + tail)
