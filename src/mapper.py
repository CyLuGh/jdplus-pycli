from jdplus.main.ws.v1.toolkit_messages_pb2 import VersionInfoDto, TsDataDto, TsPeriodDto, DescriptiveStatisticsDto, \
    DateDto, TemporalDisaggregationResultsDto, DiffuseLikelihoodStatisticsDto, DiffuseConcentratedLikelihoodDto, \
    MatrixDto
from models import VersionInfo, TsData, TsPeriod, DescriptiveStatistics, ResultStatus, TemporalDisaggregationResults, \
    DiffuseLikelihoodStatistics, DiffuseConcentratedLikelihood, Matrix

from datetime import date



class VersionInfoMapper:
    @staticmethod
    def to_model(dto: VersionInfoDto) -> VersionInfo:
        return VersionInfo(major=dto.major, minor=dto.minor, revision=dto.revision)

class TsPeriodMapper:
    @staticmethod
    def to_dto(model: TsPeriod) -> TsPeriodDto:
        dto = TsPeriodDto()
        dto.frequency = model.frequency
        dto.pos = model.position
        dto.year = model.year
        return dto

    @staticmethod
    def to_model(dto: TsPeriodDto) -> TsPeriod:
        return TsPeriod(frequency=dto.frequency, position=dto.pos, year=dto.year)

class TsDataMapper:
    @staticmethod
    def to_dto(model: TsData) -> TsDataDto:
        dto = TsDataDto()
        dto.start.frequency = model.start.frequency
        dto.start.pos = model.start.position
        dto.start.year = model.start.year
        dto.values.extend(model.values)
        return dto

    @staticmethod
    def to_model(dto: TsDataDto) -> TsData:
        start= TsPeriodMapper.to_model(dto.start)
        values= tuple(dto.values)
        return TsData(
            start= start,
            values= values
        )

class DateMapper:
    @staticmethod
    def to_dto(model: date) -> DateDto:
        dto = DateDto()
        dto.year = model.year
        dto.month = model.month
        dto.day = model.day
        return dto

class DescriptiveStatisticsMapper:
    @staticmethod
    def to_model(dto: DescriptiveStatisticsDto) -> DescriptiveStatistics:
        model = DescriptiveStatistics(
            id = dto.id,
            n= dto.n,
            n_missing= dto.nmissing,
            max= dto.max,
            min= dto.min,
            average= dto.average,
            std_dev= dto.stdev,
            q25= dto.q25,
            q50= dto.q50,
            q75= dto.q75,
            status= ResultStatus(type=dto.status.type, message=dto.status.message)
        )
        return model

class TemporalDisaggregationResultsMapper:
    @staticmethod
    def to_model(dto: TemporalDisaggregationResultsDto) -> TemporalDisaggregationResults:
        model = TemporalDisaggregationResults(
            originalSeries= TsDataMapper.to_model(dto.originalSeries),
            disaggregatedSeries= TsDataMapper.to_model(dto.disaggregatedSeries),
            stDevDisaggregatedSeries= TsDataMapper.to_model(dto.stDevDisaggregatedSeries),
            regressionEffects= TsDataMapper.to_model(dto.regressionEffects),
            statistics=DiffuseLikelihoodStatisticsMapper.to_model(dto.stats),
            likelihood=DiffuseConcentratedLikelihoodMapper.to_model(dto.likelihood)
        )
        return model

class DiffuseLikelihoodStatisticsMapper:
    @staticmethod
    def to_model(dto: DiffuseLikelihoodStatisticsDto) -> DiffuseLikelihoodStatistics:
        model = DiffuseLikelihoodStatistics(
            n_obs=dto.nobs,
            n_diffuse=dto.ndiffuse,
            n_params=dto.nparams,
            degrees_of_freedom=dto.degrees_of_freedom,
            log_likelihood=dto.log_likelihood,
            adjusted_log_likelihood=dto.adjusted_log_likelihood,
            aic=dto.aic,
            aicc=dto.aicc,
            bic=dto.bic,
            ssq=dto.ssq,
            ldet=dto.ldet,
            dcorrection=dto.dcorrection
        )
        return model

class MatrixMapper:
    @staticmethod
    def to_model(dto: MatrixDto) -> Matrix:
        model = Matrix(
            n_rows=dto.nrows,
            n_cols=dto.ncols,
            values=tuple(dto.values)
        )
        return model

class DiffuseConcentratedLikelihoodMapper:
    @staticmethod
    def to_model(dto: DiffuseConcentratedLikelihoodDto) -> DiffuseConcentratedLikelihood:
        model = DiffuseConcentratedLikelihood(
            ll=dto.ll,
            ssqerr=dto.ssqerr,
            ldet=dto.ldet,
            lddet=dto.lddet,
            n_obs=dto.nobs,
            nd=dto.nd,
            nxd=dto.nxd,
            bvar=MatrixMapper.to_model(dto.bvar),
            legacy=dto.legacy,
            scaling_factor=dto.scalingFactor,
            res=tuple(dto.res),
            b=tuple(dto.res)
        )
        return model