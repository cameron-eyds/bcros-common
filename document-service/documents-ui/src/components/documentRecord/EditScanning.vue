<script setup lang="ts">
const { scanningDetails, scanningDetailsSnapshot } = storeToRefs(useBcrosDocuments())
const hasScanningDetails = computed(() => {
  return !!scanningDetailsSnapshot.value?.scanDateTime
})

const scannedDate = computed(() => {
  return formatToReadableDate(scanningDetails.value?.scanDateTime, true)
})
</script>

<template>
  <FormWrapper
    name="document-scanning-form"
    class="pl-7"
  >
    <template #label>
      <h3>{{ $t('scanningDetails.title') }}</h3>
      <HasChangesBadge
        :baseline="scanningDetailsSnapshot"
        :current-state="scanningDetails"
      />
    </template>

    <template #form>
      <div class="grid grid-flow-row auto-rows-max">
        <UInput
          v-model="scanningDetails.accessionNumber"
          type="text"
          required
          :disabled="!hasScanningDetails"
          :placeholder="$t('scanningDetails.accessionNumber')"
        />

        <div class="grid grid-cols-4 gap-5 mt-3">
          <div class="col-span-2">
            <UInput
              v-model="scanningDetails.batchId"
              class="mt-3"
              type="text"
              required
              :disabled="!hasScanningDetails"
              :placeholder="$t('scanningDetails.batchId')"
            />
          </div>

          <div class="col-span-2">
            <UInput
              v-model="scanningDetails.pageCount"
              class="mt-3"
              type="text"
              required
              :placeholder="$t('scanningDetails.pagesToScan')"
            />
          </div>
        </div>
        <UInput
          v-model="scannedDate"
          :placeholder="$t('scanningDetails.scannedDate')"
          class="mt-3"
          :disabled="!hasScanningDetails"
          readonly
          :ui="{ base: 'border-b-[2px] border-dotted'}"
        />
      </div>
    </template>
  </FormWrapper>
</template>