from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from dplhooks.deploys import serializers
from dplhooks.deploys.essentials.deployer import ContainerDeployer


class DeployView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = serializers.DeploySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                deployer = ContainerDeployer()
                deploy_status = deployer.deploy(
                    serializer.validated_data['project'],
                    serializer.validated_data['token']
                )
                if deploy_status == 'invalid_token':
                    return Response({}, status=status.HTTP_403_FORBIDDEN)
                elif deploy_status == 'success':
                    return Response({}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'details': 'Error with deployment.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({}, status=status.HTTP_404_NOT_FOUND)
